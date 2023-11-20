import 'package:flutter/material.dart';
import 'package:mycookbook/main.dart';
import 'package:mycookbook/models/recipe.dart';

class RecipeEditPage extends StatelessWidget {
  const RecipeEditPage({super.key});

  @override
  Widget build(BuildContext context) {
    final Recipe recipe = ModalRoute.of(context)!.settings.arguments as Recipe;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Edit Recipe'),
        backgroundColor: Colors.white,
        iconTheme: const IconThemeData(color: darkBlueColor),
      ),
      body: RecipeEditForm(editedRecipe: recipe),
    );
  }
}

class RecipeEditForm extends StatefulWidget {
  const RecipeEditForm({Key? key, required this.editedRecipe})
      : super(key: key);

  final Recipe editedRecipe;

  @override
  State<RecipeEditForm> createState() => _RecipeEditFormState();
}

class _RecipeEditFormState extends State<RecipeEditForm> {
  final _formKey = GlobalKey<FormState>();
  late Recipe _editedRecipe;

  @override
  void initState() {
    super.initState();
    _editedRecipe = widget.editedRecipe.clone(); // Create a copy for editing
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      padding: const EdgeInsets.symmetric(vertical: 15, horizontal: 30),
      child: Form(
        key: _formKey,
        child: Column(
          children: <Widget>[
            TextFormField(
              decoration: const InputDecoration(labelText: 'Name'),
              initialValue: _editedRecipe.name,
              onSaved: (val) => setState(() => _editedRecipe.name = val),
              validator: (val) =>
                  (val!.isEmpty ? 'This field is required' : null),
            ),
            TextFormField(
              decoration: const InputDecoration(labelText: 'Ingredients'),
              initialValue: _editedRecipe.ingredients,
              onSaved: (val) => setState(() => _editedRecipe.ingredients = val),
              validator: (val) =>
                  (val!.isEmpty ? 'This field is required' : null),
            ),
            TextFormField(
              decoration: const InputDecoration(labelText: 'Instructions'),
              initialValue: _editedRecipe.instructions,
              onSaved: (val) =>
                  setState(() => _editedRecipe.instructions = val),
              validator: (val) =>
                  (val!.isEmpty ? 'This field is required' : null),
            ),
            TextFormField(
              decoration: const InputDecoration(labelText: 'Cooking time'),
              initialValue: _editedRecipe.cookingTime,
              onSaved: (val) => setState(() => _editedRecipe.cookingTime = val),
              validator: (val) =>
                  (val!.isEmpty ? 'This field is required' : null),
            ),
            TextFormField(
              decoration: const InputDecoration(labelText: 'Notes'),
              initialValue: _editedRecipe.notes,
              onSaved: (val) => setState(() => _editedRecipe.notes = val),
              validator: (val) =>
                  (val!.isEmpty ? 'This field is required' : null),
            ),
            // ... (rest of the form fields)
            Container(
              margin: const EdgeInsets.all(10.0),
              child: ElevatedButton(
                onPressed: () => _onSubmit(),
                style: ButtonStyle(
                  backgroundColor:
                      MaterialStateProperty.all<Color>(darkBlueColor),
                ),
                child:
                    const Text('Update', style: TextStyle(color: Colors.white)),
              ),
            ),
          ],
        ),
      ),
    );
  }

  _onSubmit() {
    var form = _formKey.currentState;
    if (form!.validate()) {
      form.save();
      // Perform the update operation
      var updatedRecipe = Recipe(
        id: widget.editedRecipe.id,
        name: _editedRecipe.name,
        ingredients: _editedRecipe.ingredients,
        instructions: _editedRecipe.instructions,
        cookingTime: _editedRecipe.cookingTime,
        notes: _editedRecipe.notes,
      );

      // Return the updated recipe to the previous screen
      Navigator.pop(context, updatedRecipe);
    }
  }
}
