package com.example.mycookbook

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.mycookbook.databinding.ActivityUpdateRecipeBinding

class UpdateRecipeActivity : AppCompatActivity() {

    private lateinit var binding: ActivityUpdateRecipeBinding
    private lateinit var db: RecipeDatabaseHelper
    private var recipeId: Int = -1

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityUpdateRecipeBinding.inflate(layoutInflater)
        setContentView(binding.root)

        db = RecipeDatabaseHelper(this)

        recipeId = intent.getIntExtra("recipe_id", -1)
        if(recipeId == -1){
            finish()
            return
        }

        val recipe = db.getRecipeById(recipeId)
        binding.updateNameEditText.setText(recipe.name)
        binding.updateIngredientsEditText.setText(recipe.ingredients)

        binding.updateSaveButton.setOnClickListener {
            val newName = binding.updateNameEditText.text.toString()
            val newIngredients = binding.updateIngredientsEditText.text.toString()
            val updatedRecipe = Recipe(recipeId, newName, newIngredients)
            db.updateRecipe(updatedRecipe)
            finish()
            Toast.makeText(this, "Changes Saved", Toast.LENGTH_SHORT).show()
        }
    }
}