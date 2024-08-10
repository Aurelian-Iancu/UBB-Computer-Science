using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerBall2 : MonoBehaviour
{
    private float forceMagnitude = Constants.playerForce;
    private Rigidbody rb;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        if (Input.GetKey(KeyCode.W))
        {
            rb.AddForce(Vector3.forward * forceMagnitude, ForceMode.Impulse);
        }
        else if (Input.GetKey(KeyCode.S))
        {
            rb.AddForce(Vector3.back * forceMagnitude, ForceMode.Impulse);
        }
        else if (Input.GetKey(KeyCode.A))
        {
            rb.AddForce(Vector3.left * forceMagnitude, ForceMode.Impulse);
        }
        else if (Input.GetKey(KeyCode.D))
        {
            rb.AddForce(Vector3.right * forceMagnitude, ForceMode.Impulse);
        }
    }
}
