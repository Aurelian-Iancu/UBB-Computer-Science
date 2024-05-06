package org.example.features.search;

import net.serenitybdd.junit.runners.SerenityRunner;
import net.thucydides.core.annotations.Issue;
import net.thucydides.core.annotations.Managed;
import net.thucydides.core.annotations.Pending;
import net.thucydides.core.annotations.Steps;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;

import org.example.steps.serenity.EndUserSteps;

@RunWith(SerenityRunner.class)
public class SearchByKeywordStory {

    @Managed(uniqueSession = true)
    public WebDriver webdriver;

    @Steps
    public EndUserSteps anna;

    @Issue("#WIKI-1")
    @Test
    public void searching_by_keyword_apple_should_display_the_corresponding_article() {
        anna.is_the_home_page();
        anna.looks_for("apple");
        anna.should_see_definition("A common, round fruit produced by the tree Malus domestica, cultivated in temperate climates.");

    }

    @Test
    public void searching_by_keyword_banana_should_display_the_corresponding_article() {
        anna.is_the_home_page();
        anna.looks_for("pear");
        anna.should_see_definition("An edible fruit produced by the pear tree, similar to an apple but typically elongated towards the stem.");
                                   // An edible fruit produced by the pear tree, similar to an apple but typically elongated towards the stem.
    }

    @Test
    public void searching_by_keyword_horse_should_display_the_corresponding_article(){
        anna.is_the_home_page();
        anna.looks_for("horse");
        anna.should_see_definition("A hoofed mammal, Equus ferus caballus, often used throughout history for riding and draft work.");
    }

    @Test
    public void searching_by_keyword_ball_should_display_the_corresponding_article(){
        anna.is_the_home_page();
        anna.looks_for("ball");
        anna.should_see_definition("A solid or hollow sphere, or roughly spherical mass.");
    }

    @Pending @Test
    public void searching_by_ambiguious_keyword_should_display_the_disambiguation_page() {
    }
} 