using UnityEngine.UI;
using UnityEngine.SceneManagement;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    public GameObject panel1;
    public GameObject optionsPanel;
    public GameObject wins;
    public GameObject controls;
    public Text[] scores;

    void Start()
    {
        
    }

    public void StartGame()
    {
        Debug.Log("Enter Game");
        SceneManager.LoadScene("Game");
    }

    public void Options()
    {
        Debug.Log("Options");
        panel1.SetActive(false);
        optionsPanel.SetActive(true);
    }
    
    public void ExitOptions()
    {
        Debug.Log("Exit Options");
        panel1.SetActive(true);
        optionsPanel.SetActive(false);
    }

    public void Wins()
    {
        Debug.Log("Wins");
        panel1.SetActive(false);

        for (int i = 0; i < Constants.maxNumberOfPlayers; i++)
            scores[i].text = PlayerPrefs.GetInt(i + "wins").ToString();

        wins.SetActive(true);
    }

    public void ExitWins()
    {
        Debug.Log("Exit Wins");
        panel1.SetActive(true);
        wins.SetActive(false);
    }

    public void Controls()
    {
        Debug.Log("Controls");
        panel1.SetActive(false);
        controls.SetActive(true);
    }

    public void ExitControls()
    {
        Debug.Log("Exit Controls");
        panel1.SetActive(true);
        controls.SetActive(false);
    }

    public void ExitGame()
    {
        Debug.Log("Exit game");
        Application.Quit();
    }
}
