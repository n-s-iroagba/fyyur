const aform=document.getElementById(createartist)
const form=new FormData(aform)
fetch('/login', {
    method: 'POST',
    body: form})