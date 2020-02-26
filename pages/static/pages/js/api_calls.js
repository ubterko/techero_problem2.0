/*contains code for api calls

xhl = new XMLHttpRequest();

xhl.open('POST', 'http://127.0.0.1:8000/api/register/', true)

xhl.load = function(){
 if (this.status === 200){
   console.log(JSON.parse(this.responseText));
 }
}

xhl.send();
*/

const userAction = asyn () => {
  const response = await fetch('http://example.com');
  const myJson = await response.json();
}
