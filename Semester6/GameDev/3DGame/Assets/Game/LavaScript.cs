using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class LavaScript : MonoBehaviour
{
    public Text Text;
    private int[] alive;

    IEnumerator EndGame(int lastAlive)
    {
        Text.enabled = true;
        Text.text = "Winner: " + IndexToTag(lastAlive);
        Debug.Log("End game");

        yield return new WaitForSeconds(2);

        GameOver.EndGame(lastAlive);
    }

    void Start()
    {
        alive = new int[Constants.maxNumberOfPlayers];
        Text.enabled = false;
        for (int i = 0; i < Constants.maxNumberOfPlayers; i++)
        {
            Debug.Log(i + " " + PlayerPrefs.GetInt(i.ToString()));
            alive[i] = PlayerPrefs.GetInt(i.ToString());
        }
    }

    private void OnCollisionEnter(Collision collision)
    {
        // kill and destroy
        string tag = collision.gameObject.tag;
        Debug.Log(tag);
        int index = TagToIndex(tag);
        alive[index] = -1;
        Destroy(collision.gameObject);

        if(CheckGameOver())
        {
            int lastAlive = LastAlive();
            if (lastAlive != -1)
                StartCoroutine(EndGame(lastAlive));
        }
    }

    private int TagToIndex(string tag)
    {
        switch(tag)
        {
            case "Player1":
                return 0;
            case "Player2":
                return 1;
            case "Player3":
                return 2;
            case "Bot1":
                return 3;
            case "Bot2":
                return 4;
            case "Bot3":
                return 5;
        }
        return -1;
    }

    private string IndexToTag(int index)
    {
        switch (index)
        {
            case 0:
                return "Player1";
            case 1:
                return "Player2";
            case 2:
                return "Player3";
            case 3:
                return "Bot1";
            case 4:
                return "Bot2";
            case 5:
                return "Bot3";
        }
        return "";
    }

    private bool CheckGameOver()
    {
        int aliveCount = 0;
        for (int i = 0; i < Constants.maxNumberOfPlayers; i++)
            if (alive[i] > -1)
                ++aliveCount;
        return aliveCount <= 1;
    }

    private int LastAlive()
    {
        for (int i = 0; i < Constants.maxNumberOfPlayers; i++)
            if (alive[i] > -1)
                return i;
        return -1;
    }
}
