var all_users = document.getElementById('myUL');
var users = all_users.getElementsByTagName('ulx');
l = []
for (x = 0 ; x < users.length ; x++) {
  var h = users[x]
  l.push(h)
}

for (x = 0 ; x < users.length ; x++ ) {
  var user = users[x]
  var items = user.getElementsByTagName('li');
  var count = items.length
  if (count != 0) {

  
    var result = count
    var div = document.getElementById(user)
    var p = document.createElement('a')
    var num = document.createTextNode(' ' + result)
    p.append(num)
    user = user.outerHTML
    user = user.slice(9)
    var cutting = user.indexOf('>')
    user = user.slice(0 , cutting - 1)
    user_text = document.getElementById(user + 'text').className="bold- remove-edit-2"
    body = user + 'body'
    user = user + '1'
    if ( p.text >= 1 && p.text <= 9 ) {
      document.getElementById(body).className = "bord3 media content-section";
      document.getElementById(user).className = "badge";
      document.getElementById(user).innerHTML = p.text
    } if (p.text >= 10) {
      document.getElementById(body).className = "back bord3 media content-section";
      document.getElementById(user).className = "badge-9";
      document.getElementById(user).innerHTML = '9+'
    } else {

    }
    //document.getElementById(user).appendChild(p)
  } else {
    continue
  }
}
for (z = 0 ; z < users.length ; z++) {
  var user  = users[z]
  user = user.outerHTML
  user = user.slice(9)
  var cut_by = user.indexOf('>')
  user = user.slice(0 , cut_by - 1)
  user = user + 'text'
  user_text = document.getElementById(user)
  text_needed = user_text.innerHTML
  if (text_needed.length >= 74) {
    text_needed = text_needed.slice(0 , 74)
    document.getElementById(user).innerHTML = text_needed + '...'
  } else {
      continue
  }
}

for (var i = 0 ; i < 100 ; i++) {
  document.getElementById('changeresult').remove();

}

function myFunction() {
    // Declare variables
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('liu');
  
    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("spani")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        li[i].style.display = "";
      } else {
        li[i].style.display = "none";
      }
    }
  }