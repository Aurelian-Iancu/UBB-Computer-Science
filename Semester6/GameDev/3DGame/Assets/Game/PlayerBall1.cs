using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerBall1 : MonoBehaviour
{
    private float forceMagnitude = Constants.playerForce;
    private Rigidbody rb;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.UpArrow))
        {
            rb.AddForce(Vector3.forward * forceMagnitude, ForceMode.Impulse);
        }
        else if (Input.GetKey(KeyCode.DownArrow))
        {
            rb.AddForce(Vector3.back * forceMagnitude, ForceMode.Impulse);
        }
        else if (Input.GetKey(KeyCode.LeftArrow))
        {
            rb.AddForce(Vector3.left * forceMagnitude, ForceMode.Impulse);
        }
        else if (Input.GetKey(KeyCode.RightArrow))
        {
            rb.AddForce(Vector3.right * forceMagnitude, ForceMode.Impulse);
        }
    }
}
