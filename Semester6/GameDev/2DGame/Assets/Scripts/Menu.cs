using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Menu : MonoBehaviour
{
    public string level1;
    public string level2;
    public string startGame;
    public void StartLevel1()
    {
        SceneManager.LoadScene(level1);
    }

    public void StartLevel2()
    {
        SceneManager.LoadScene(level2);
    }

    public void StartGame()
    {
        SceneManager.LoadScene(startGame);
    }

    public void QuitGame()
    {
        Application.Quit();
    }
}
