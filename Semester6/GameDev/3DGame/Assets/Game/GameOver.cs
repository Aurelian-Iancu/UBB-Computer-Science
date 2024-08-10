using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameOver : MonoBehaviour
{
    public static void EndGame(int winner)
    {
        Debug.Log("End Game, winner : " + winner);

        // update leaderboard
        string key = winner + "wins";
        int wins = PlayerPrefs.GetInt(key);
        PlayerPrefs.SetInt(key, wins + 1);
        PlayerPrefs.Save();
        SceneManager.LoadScene("PlayScene");
    }
}
