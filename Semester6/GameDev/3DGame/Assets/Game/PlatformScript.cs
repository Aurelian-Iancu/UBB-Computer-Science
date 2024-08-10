using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlatformScript : MonoBehaviour
{
    private float shrinkRate = Constants.shrinkPlatformRate; // Rate at which the cube shrinks
    private const float shrinkRateIncrease = Constants.shrinkPlatformRate; // increase for the rate once in a while
    private const float shrinkInterval = Constants.shrinkPlatformInterval; // Time interval between each shrink operation

    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(ShrinkPlatform());
    }

    IEnumerator ShrinkPlatform()
    {
        int increase = 0;
        while (true)
        {
            if(increase % 10 == 0)
            {
                increase = 0;
                shrinkRate += shrinkRateIncrease;
            }
            // Wait for the specified interval
            yield return new WaitForSeconds(shrinkInterval);

            // Shrink the cube on the x and z axes
            Vector3 currentScale = transform.localScale;
            currentScale.x -= shrinkRate;
            currentScale.z -= shrinkRate;

            // Ensure the scale doesn't become negative
            currentScale.x = Mathf.Max(0, currentScale.x);
            currentScale.z = Mathf.Max(0, currentScale.z);

            // Update the scale of the cube
            transform.localScale = currentScale;
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
