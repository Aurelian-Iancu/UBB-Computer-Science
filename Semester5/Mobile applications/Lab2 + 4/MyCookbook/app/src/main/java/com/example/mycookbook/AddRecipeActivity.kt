package com.example.mycookbook

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.example.mycookbook.databinding.ActivityAddRecipeBinding

class AddRecipeActivity : AppCompatActivity() {

    private lateinit var binding: ActivityAddRecipeBinding
    private lateinit var db: RecipeDatabaseHelper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityAddRecipeBinding.inflate(layoutInflater)

        setContentView(binding.root)

        db = RecipeDatabaseHelper(this)

        binding.saveButton.setOnClickListener{
            val name = binding.nameEditText.text.toString()
            val ingredients = binding.ingredientsEditText.text.toString()
            val recipe = Recipe(0, name, ingredients)
            db.insertRecipe(recipe)
            finish()
            Toast.makeText(this, "Recipe Saved", Toast.LENGTH_SHORT).show()
        }
    }
}