class Recipe {
  static const tableRecipe = 'recipes';
  static const colId = 'id';
  static const colName = 'name';
  static const colIngredients = 'ingredients';
  static const colInstructions = 'instructions';
  static const colCookingTime = 'cookingTime';
  static const colNotes = 'notes';

  int? id;
  String? name;
  String? ingredients;
  String? instructions;
  String? cookingTime;
  String? notes;

  // Constructor
  Recipe({
    required this.id,
    required this.name,
    required this.ingredients,
    required this.instructions,
    required this.cookingTime,
    required this.notes,
  });

  // Named constructor with no parameters
  Recipe.empty()
      : id = 0,
        name = '',
        ingredients = '',
        instructions = '',
        cookingTime = '',
        notes = '';

  Map<String, dynamic> toMap() {
    var map = <String, dynamic>{
      colName: name,
      colIngredients: ingredients,
      colInstructions: instructions,
      colCookingTime: cookingTime,
      colNotes: notes
    };
    if (id != null) {
      map[colId] = id;
    }
    return map;
  }

  Recipe.fromMap(Map<String, dynamic> map) {
    id = map[colId];
    name = map[colName];
    ingredients = map[colIngredients];
    instructions = map[colInstructions];
    cookingTime = map[colCookingTime];
    notes = map[colNotes];
  }

  // Copy constructor
  Recipe.copy(Recipe other)
      : id = other.id,
        name = other.name,
        ingredients = other.ingredients,
        instructions = other.instructions,
        cookingTime = other.cookingTime,
        notes = other.notes;

  Recipe clone() => Recipe.copy(this);
}
