const menu = document.getElementById("menu");

const ul = document.createElement("ul");

for (let i = 1; i <= 5; i++) {
  const li = document.createElement("li");
  const p = document.createElement("p");
  p.textContent = `Submenu ${i}`;

  const subUl = document.createElement("ul");
  const numSubItems = Math.floor(Math.random() * (5 - 3 + 1)) + 3; // Generate a random number of submenu items (between 3 and 5)
  for (let j = 1; j <= numSubItems; j++) {
    const subLi = document.createElement("li");
    const subP = document.createElement("p");
    subP.textContent = `Component ${j} of Submenu ${i}`;
    subLi.appendChild(subP);
    subUl.appendChild(subLi);
  }

  p.addEventListener("click", function () {
    if(subUl.style.display === "none"){
        subUl.style.display = "block";
      } else {
        subUl.style.display = "none";
      }
  });

  li.appendChild(p);
  li.appendChild(subUl);
  ul.appendChild(li);
}

const menuHeader = document.getElementById("menu-header");
menuHeader.addEventListener("click", function () {
  if(ul.style.display === "none"){
    ul.style.display = "block";
  } else {
    ul.style.display = "none";
  }
});

menu.appendChild(ul);