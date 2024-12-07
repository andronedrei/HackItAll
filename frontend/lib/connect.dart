// import 'dart:convert';
import 'package:http/http.dart' as http;

Future<void> fetchData() async {
  final url = Uri.parse('http://127.0.0.1:8000/api/mymodel/');
  final response = await http.get(url);

  if (response.statusCode == 200) {
    // final data = jsonDecode(response.body);
    // print(data); // Use this data in your app
  } else {
    throw Exception('Failed to load data');
  }
}
