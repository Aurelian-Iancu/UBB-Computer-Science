using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerBall3 : MonoBehaviour
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
        if (Input.GetKey(KeyCode.I))
        {
            rb.AddForce(Vector3.forward * forceMagnitude, ForceMode.Impulse);
        }
        else if (Input.GetKey(KeyCode.K))
        {
            rb.AddForce(Vector3.back * forceMagnitude, ForceMode.Impulse);
        }
        else if (Input.GetKey(KeyCode.J))
        {
            rb.AddForce(Vector3.left * forceMagnitude, ForceMode.Impulse);
        }
        else if (Input.GetKey(KeyCode.L))
        {
            rb.AddForce(Vector3.right * forceMagnitude, ForceMode.Impulse);
        }
    }
}
