import 'dart:async';
import 'dart:convert';
import 'package:web_socket_client/web_socket_client.dart';

class ChatWebService {
  static final _instance = ChatWebService._internal();
  WebSocket? _socket;
  StreamSubscription? _socketSubscription;

  factory ChatWebService() => _instance;

  ChatWebService._internal() {
    // Create broadcast streams to allow multiple listeners
    _searchResultController =
        StreamController<Map<String, dynamic>>.broadcast();
    _contentController = StreamController<Map<String, dynamic>>.broadcast();
  }

  late final StreamController<Map<String, dynamic>> _searchResultController;
  late final StreamController<Map<String, dynamic>> _contentController;

  Stream<Map<String, dynamic>> get searchResultStream =>
      _searchResultController.stream;
  Stream<Map<String, dynamic>> get contentStream => _contentController.stream;

  void connect() {
    // Close existing connection if any
    disconnect();

    // Connect to WebSocket
    _socket = WebSocket(Uri.parse("ws://localhost:8000/ws/chat"));

    _socketSubscription = _socket!.messages.listen((message) {
      print("Received message: $message");
      try {
        final data = json.decode(message);
        print("Received JSON message: $data");
        if (data['type'] == 'search_result') {
          _searchResultController.add(data);
        } else if (data['type'] == 'content') {
          _contentController.add(data);
        }
      } catch (e) {
        print("Error processing message: $e");
      }
    }, onError: (error) {
      print("WebSocket error: $error");
    }, onDone: () {
      print("WebSocket connection closed");
    });
  }

  void disconnect() {
    _socketSubscription?.cancel();
    _socketSubscription = null;
    _socket?.close();
    _socket = null;
  }

  void chat(String query) {
    print("Sending query: $query");
    print("Socket: $_socket");
    try {
      if (_socket != null) {
        _socket!.send(json.encode({'query': query}));
      } else {
        print("Socket is null, reconnecting");
        connect();
        // Add a small delay before sending the message
        Future.delayed(Duration(milliseconds: 500), () {
          if (_socket != null) {
            _socket!.send(json.encode({'query': query}));
          }
        });
      }
    } catch (e) {
      print("Error sending message: $e");
    }
  }

  // Call this method when the app is being terminated
  void dispose() {
    disconnect();
    _searchResultController.close();
    _contentController.close();
  }
}
