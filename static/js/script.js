// Example POST method implementation:
async function postData(url = "", data = {}) {
    const response = await fetch(url, {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin     
      headers: {
        "Content-Type": "application/json",   
      }, body: JSON.stringify(data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }
  
  postData("https://example.com/answer", { answer: 42 }).then((data) => {
    console.log(data); // JSON data parsed by `data.json()` call
  });
  


sendButton.addEventListener("click", async() => {
    
    questionInput = document.getElementById("questionInput").value
    document.getElementById("questionInput").value = "";
    document.querySelector(".right2").style.display = "block"
    document.querySelector(".right1").style.display = "none"

    console.log(questionInput)
    document.getElementById("question1").innerHTML = questionInput;
    document.getElementById("question2").innerHTML = questionInput;
    //get the answer

    let result = await postData('/api',{"question":questionInput})
    solution.innerHTML = result.result
})