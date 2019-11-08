//contains code for api calls

xhl = new XMLHttpRequest();

xhl.open('GET', '', true)

xhl.load = function(){
  if (this.status === 200){
    console.log(JSON.parse(this.responseText));
  }
}

xhl.send();
