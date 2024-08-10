using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;
using UnityEngine.EventSystems;

public class OptionsScript : MonoBehaviour
{
    public Toggle[] toggles;
    public Image[] images;
    public Sprite[] sprites;
    void Start()
    {
        if(!PlayerPrefs.HasKey("NotFirstTime"))
        {
            PlayerPrefs.SetInt("NotFirstTime", 1);
            for (int i = 0; i < toggles.Length; ++i)
            {
                PlayerPrefs.SetInt(i.ToString(), -1);
                PlayerPrefs.SetInt(i + "wins", 0);
            }
            PlayerPrefs.Save();
        }

        for(int i = 0; i < toggles.Length; ++i)
        {
            int index = i;
            int spriteIndex = PlayerPrefs.GetInt(index.ToString());
            if (spriteIndex != -1)
            {
                toggles[index].isOn = true;
                images[index].enabled = true;
                images[index].sprite = sprites[spriteIndex];
                images[index].material = images[index].defaultMaterial;
            }

            toggles[index].onValueChanged.AddListener(isOn =>
            {
                if (isOn)
                {
                    images[index].enabled = true;
                    images[index].sprite = sprites[0];
                    images[index].material = images[index].defaultMaterial;
                    PlayerPrefs.SetInt(index.ToString(), 0);
                }
                else
                {
                    images[index].enabled = false;
                    PlayerPrefs.SetInt(index.ToString(), -1);
                }
                PlayerPrefs.Save();
            });
        }
    }

    public void OnClick0()
    {
        var sprite = images[0].sprite;
        int index = -1;
        for (int i = 0; i < sprites.Length; ++i)
            if (sprite.Equals(sprites[i]))
                index = i;
        ++index;
        if (index >= sprites.Length)
            index = 0;

        images[0].sprite = sprites[index];
        PlayerPrefs.SetInt("0", index);
        PlayerPrefs.Save();
    }

    public void OnClick1()
    {
        var sprite = images[1].sprite;
        int index = -1;
        for (int i = 0; i < sprites.Length; ++i)
            if (sprite.Equals(sprites[i]))
                index = i;
        ++index;
        if (index >= sprites.Length)
            index = 0;

        images[1].sprite = sprites[index];
        PlayerPrefs.SetInt("1", index);
        PlayerPrefs.Save();
    }

    public void OnClick2()
    {
        var sprite = images[2].sprite;
        int index = -1;
        for (int i = 0; i < sprites.Length; ++i)
            if (sprite.Equals(sprites[i]))
                index = i;
        ++index;
        if (index >= sprites.Length)
            index = 0;

        images[2].sprite = sprites[index];
        PlayerPrefs.SetInt("2", index);
        PlayerPrefs.Save();
    }

    public void OnClick3()
    {
        var sprite = images[3].sprite;
        int index = -1;
        for (int i = 0; i < sprites.Length; ++i)
            if (sprite.Equals(sprites[i]))
                index = i;
        ++index;
        if (index >= sprites.Length)
            index = 0;

        images[3].sprite = sprites[index];
        PlayerPrefs.SetInt("3", index);
        PlayerPrefs.Save();
    }

    public void OnClick4()
    {
        var sprite = images[4].sprite;
        int index = -1;
        for (int i = 0; i < sprites.Length; ++i)
            if (sprite.Equals(sprites[i]))
                index = i;
        ++index;
        if (index >= sprites.Length)
            index = 0;

        images[4].sprite = sprites[index];
        PlayerPrefs.SetInt("4", index);
        PlayerPrefs.Save();
    }

    public void OnClick5()
    {
        var sprite = images[5].sprite;
        int index = -1;
        for (int i = 0; i < sprites.Length; ++i)
            if (sprite.Equals(sprites[i]))
                index = i;
        ++index;
        if (index >= sprites.Length)
            index = 0;

        images[5].sprite = sprites[index];
        PlayerPrefs.SetInt("5", index);
        PlayerPrefs.Save();
    }
}
