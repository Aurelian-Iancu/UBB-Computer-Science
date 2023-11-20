import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:mycookbook/models/recipe.dart';
import 'package:mycookbook/recipe_edit_page.dart';

const darkBlueColor = Color(0xff486579);

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My cookbook',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: darkBlueColor),
        useMaterial3: true,
      ),
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => const MyHomePage(title: 'My cookbook'),
        '/edit': (context) => const RecipeEditPage(),
      },
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final _formKey = GlobalKey<FormState>();
  Recipe _recipe = Recipe.empty();
  List<Recipe> _recipes = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[200],
      appBar: AppBar(
        backgroundColor: Colors.white,
        title: Center(
          child: Text(
            widget.title,
            style: TextStyle(color: darkBlueColor),
          ),
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[_form(), _list()],
        ),
      ),
    );
  }

  _form() => Container(
        color: Colors.white,
        padding: EdgeInsets.symmetric(vertical: 15, horizontal: 30),
        child: Form(
          key: _formKey,
          child: Column(
            children: <Widget>[
              TextFormField(
                decoration: InputDecoration(labelText: 'Name'),
                onSaved: (val) => setState(() => _recipe.name = val),
                validator: (val) =>
                    (val!.isEmpty ? 'This field is required' : null),
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Ingredients'),
                onSaved: (val) => setState(() => _recipe.ingredients = val),
                validator: (val) =>
                    (val!.isEmpty ? 'This field is required' : null),
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Instructions'),
                onSaved: (val) => setState(() => _recipe.instructions = val),
                validator: (val) =>
                    (val!.isEmpty ? 'This field is required' : null),
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Cooking time'),
                onSaved: (val) => setState(() => _recipe.cookingTime = val),
                validator: (val) =>
                    (val!.isEmpty ? 'This field is required' : null),
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Notes'),
                onSaved: (val) => setState(() => _recipe.notes = val),
                validator: (val) =>
                    (val!.isEmpty ? 'This field is required' : null),
              ),
              Container(
                margin: EdgeInsets.all(10.0),
                child: ElevatedButton(
                  onPressed: () => _onSubmit(),
                  style: ButtonStyle(
                    backgroundColor:
                        MaterialStateProperty.all<Color>(darkBlueColor),
                  ),
                  child: Text('Submit', style: TextStyle(color: Colors.white)),
                ),
              )
            ],
          ),
        ),
      );

  _onSubmit() {
    var form = _formKey.currentState;
    if (form!.validate()) {
      form.save();
      setState(() {
        _recipes.add(Recipe(
          id: DateTime.now().millisecondsSinceEpoch, // Unique ID for simplicity
          name: _recipe.name,
          ingredients: _recipe.ingredients,
          instructions: _recipe.instructions,
          cookingTime: _recipe.cookingTime,
          notes: _recipe.notes,
        ));
      });
      form.reset();
    }
  }

  _onUpdate(Recipe recipe) async {
    final updatedRecipe =
        await Navigator.pushNamed(context, '/edit', arguments: recipe)
            as Recipe?;

    if (updatedRecipe != null) {
      setState(() {
        // Find the index of the updated recipe in the list
        final index = _recipes.indexWhere((r) => r.id == recipe.id);

        // Update the recipe in the list
        if (index != -1) {
          _recipes[index] = updatedRecipe;
        }
      });
    }
  }

  _onDelete(Recipe recipe) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Delete Confirmation'),
          content: Text('Are you sure you want to delete ${recipe.name}?'),
          actions: <Widget>[
            TextButton(
              onPressed: () {
                // Dismiss the dialog
                Navigator.of(context).pop();
              },
              child: Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                // Perform the delete operation
                setState(() {
                  _recipes.remove(recipe);
                });
                // Dismiss the dialog
                Navigator.of(context).pop();
              },
              child: Text('Delete'),
            ),
          ],
        );
      },
    );
  }

  _list() => Expanded(
        child: Card(
          margin: EdgeInsets.fromLTRB(20, 30, 20, 0),
          child: ListView.builder(
            padding: EdgeInsets.all(8),
            itemBuilder: (context, index) {
              final recipe = _recipes[index];
              return Column(
                children: <Widget>[
                  ListTile(
                    leading: Icon(
                      Icons.account_circle,
                      color: darkBlueColor,
                      size: 40.0,
                    ),
                    title: Text(
                      recipe.name!.toUpperCase(),
                      style: TextStyle(
                        color: darkBlueColor,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    subtitle: Text(recipe.cookingTime!),
                    onTap: () => _onUpdate(recipe),
                    trailing: IconButton(
                      icon: Icon(
                        Icons.delete,
                        color: darkBlueColor,
                      ),
                      onPressed: () => _onDelete(recipe),
                    ),
                  ),
                  Divider(
                    height: 5.0,
                  ),
                ],
              );
            },
            itemCount: _recipes.length,
          ),
        ),
      );
}
