using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnBalls : MonoBehaviour
{
    public GameObject platform;
    public Material[] materials;

    private float radius = 1f; // Radius of the circle

    // Start is called before the first frame update
    void Start()
    {
        SpawnEntities();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void SpawnEntities()
    {
        Vector3 centerPosition = Vector3.zero; //platform.transform.position;
        float angleStep = 360f / CountPlayers(); // Angle between each entity
        float ballScale = 1f;

        for (int i = 0; i < Constants.maxNumberOfPlayers; i++)
        {
            float angle = i * angleStep; // Calculate angle for this entity

            // Calculate position in circle using trigonometry
            float x = centerPosition.x + Mathf.Cos(angle * Mathf.Deg2Rad) * radius;
            float y = centerPosition.y + platform.transform.localScale.y + ballScale + 0.1f;
            float z = centerPosition.z + Mathf.Sin(angle * Mathf.Deg2Rad) * radius;

            int materialIndex = PlayerPrefs.GetInt(i.ToString());
            if(materialIndex != -1)
            {
                // Spawn sphere at calculated position
                GameObject newSphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
                newSphere.gameObject.AddComponent<Rigidbody>();
                newSphere.transform.position = new Vector3(x, y, z);
                newSphere.transform.localScale = new Vector3(ballScale, ballScale, ballScale); // Set scale as needed
                Debug.Log("Spawn");
                if (i == 0)
                {
                    newSphere.gameObject.AddComponent<PlayerBall1>();
                    newSphere.gameObject.tag = "Player1";
                    MeshRenderer renderer = newSphere.GetComponent<MeshRenderer>();
                    renderer.material = materials[materialIndex];
                }
                else if (i == 1)
                {
                    newSphere.gameObject.AddComponent<PlayerBall2>();
                    newSphere.gameObject.tag = "Player2";
                    MeshRenderer renderer = newSphere.GetComponent<MeshRenderer>();
                    renderer.material = materials[materialIndex];
                }
                else if (i == 2)
                {
                    newSphere.gameObject.AddComponent<PlayerBall3>();
                    newSphere.gameObject.tag = "Player3";
                    MeshRenderer renderer = newSphere.GetComponent<MeshRenderer>();
                    renderer.material = materials[materialIndex];
                }
                else
                {
                    newSphere.gameObject.AddComponent<BallAI>();
                    newSphere.gameObject.tag = "Bot" + (i - 2);
                    MeshRenderer renderer = newSphere.GetComponent<MeshRenderer>();
                    renderer.material = materials[materialIndex];
                }
            }
        }
    }

    private int CountPlayers()
    {
        int count = 0;
        for (int i = 0; i < Constants.maxNumberOfPlayers; i++)
        {
            if (PlayerPrefs.GetInt(i.ToString()) != -1)
                ++count;
        }
        return count;
    }
}
