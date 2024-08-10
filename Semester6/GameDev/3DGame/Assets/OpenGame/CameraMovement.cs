using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{
    public Transform target; // The cube around which the camera will orbit
    private float orbitSpeed = 2f; // Speed of the orbit movement
    private float orbitRadius = 5f; // Radius of the orbit circle

    private float angle = 0f; // Current angle of rotation

    void Update()
    {
        // Calculate the position of the camera in the orbit circle
        float x = target.position.x + orbitRadius * Mathf.Cos(angle * Mathf.Deg2Rad);
        float z = target.position.z + orbitRadius * Mathf.Sin(angle * Mathf.Deg2Rad);

        // Update the position of the camera
        transform.position = new Vector3(x, target.position.y + orbitRadius, z);

        // Look at the target cube
        transform.LookAt(target);

        // Increment the angle for the next frame
        angle += orbitSpeed * Time.deltaTime;

        // Reset angle if it goes beyond 360 degrees
        if (angle >= 360f)
        {
            angle -= 360f;
        }
    }
}
