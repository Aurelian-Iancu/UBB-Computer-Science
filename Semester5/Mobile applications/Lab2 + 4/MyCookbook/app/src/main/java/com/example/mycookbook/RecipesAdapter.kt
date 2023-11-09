import android.content.Context
import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.recyclerview.widget.RecyclerView
import com.example.mycookbook.R
import com.example.mycookbook.Recipe
import com.example.mycookbook.RecipeDatabaseHelper
import com.example.mycookbook.UpdateRecipeActivity

class RecipesAdapter(private var recipes: List<Recipe>, context: Context) :
    RecyclerView.Adapter<RecipesAdapter.RecipeViewHolder>() {

    private val db: RecipeDatabaseHelper = RecipeDatabaseHelper(context)

    class RecipeViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView){
        val nameTextView: TextView = itemView.findViewById(R.id.nameTextView)
        val ingredientsTextView: TextView = itemView.findViewById(R.id.ingredientsTextView)
        var updateButton: ImageView = itemView.findViewById(R.id.updateButton)
        var deleteButton: ImageView = itemView.findViewById(R.id.deleteButton)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecipeViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.recipe_item, parent, false)
        return RecipeViewHolder(view)
    }

    override fun getItemCount(): Int {
        return recipes.size
    }

    override fun onBindViewHolder(holder: RecipeViewHolder, position: Int) {
        val recipe = recipes[position]
        holder.nameTextView.text = recipe.name
        holder.ingredientsTextView.text = recipe.ingredients

        holder.updateButton.setOnClickListener {
            val intent = Intent(holder.itemView.context, UpdateRecipeActivity::class.java).apply {
                putExtra("recipe_id", recipe.id)
            }
            holder.itemView.context.startActivity(intent)
        }

        holder.deleteButton.setOnClickListener {
            db.deleteRecipe(recipe.id)
            refreshData(db.getAllRecipes())
            Toast.makeText(holder.itemView.context, "Note deleted", Toast.LENGTH_SHORT).show()
        }
    }

    fun refreshData(newRecipes: List<Recipe>){
        recipes = newRecipes
        notifyDataSetChanged()
    }
}