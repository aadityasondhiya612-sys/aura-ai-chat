function send(){
    let input=document.getElementById("input");
    let msg=input.value;

    if(!msg) return;

    addMessage(msg,"user");
    input.value="";

    fetch('/chat',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({message:msg})
    })
    .then(res=>res.json())
    .then(data=>{
        addMessage(data.reply,"bot");
    });
}

function addMessage(text,type){
    let box=document.getElementById("chat-box");

    let div=document.createElement("div");
    div.classList.add("message",type);
    div.innerText=text;

    box.appendChild(div);
}

function newChat(){
    document.getElementById("chat-box").innerHTML="";
}
