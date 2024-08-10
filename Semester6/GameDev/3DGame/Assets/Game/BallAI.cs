using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BallAI : MonoBehaviour
{
    public float forceMagnitude = 5f;
    private const float interval = 0.7f; // seconds

    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(ApplyForcePeriodically());
    }

    IEnumerator ApplyForcePeriodically()
    {
        while (true)
        {
            yield return new WaitForSeconds(interval);

            // Calculate direction towards the center (0, 0, 0)
            Vector3 centerDirection = -transform.position.normalized;

            // Access the Rigidbody component of the current GameObject
            Rigidbody rb = GetComponent<Rigidbody>();

            // Apply force towards the center
            rb.AddForce(centerDirection * forceMagnitude, ForceMode.Impulse);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
