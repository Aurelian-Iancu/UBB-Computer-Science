package org.example.pages;

import net.serenitybdd.core.annotations.findby.FindBy;
import net.serenitybdd.core.pages.PageObject;
import net.serenitybdd.core.pages.WebElementFacade;
import net.thucydides.core.annotations.DefaultUrl;
import org.openqa.selenium.By;

import java.util.List;
import java.util.stream.Collectors;

@DefaultUrl("https://www.emag.ro/")
public class EmagPage extends PageObject {
    @FindBy(id="searchboxTrigger")
    private WebElementFacade search;
    @FindBy(css=".searchbox-submit-button")
    private WebElementFacade lookupButton;

    public void enter_keywords(String keyword) {
        search.type(keyword);
    }

    public void filter() {
        WebElementFacade cookieButton = find(By.xpath("/html/body/div[7]/div/div[2]/button[1]"));
        cookieButton.click();
        WebElementFacade filterButton = find(By.cssSelector("[data-name=\"Sub 50\"]"));
        filterButton.click();
    }

    public void lookup_terms() {
        lookupButton.click();
    }

    public List<String> getItems() {
        WebElementFacade itemsList = find(By.id("card_grid"));
        return itemsList.findElements(By.cssSelector(".card-item")).stream()
                .map( element -> element.getAttribute("data-name") )
                .collect(Collectors.toList());
    }

    public List<Double> getItemsPrices() {
        WebElementFacade itemsList = find(By.id("card_grid"));
        return itemsList.findElements(By.cssSelector(".product-new-price")).stream()
                .map( element -> Double.parseDouble(element.getText().replaceAll("[Ll][eE][iI]", "").replaceAll(",", ".").trim() ))
                .collect(Collectors.toList());
    }
}