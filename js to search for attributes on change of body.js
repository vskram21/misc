$('body').bind("DOMSubtreeModified", function(){var el = document.body;
var childrens = el.children;
for (var i = 0; atts = childrens.length;i++){
   if(childrens[i].getAttribute('data-target'))
   {
    alert(childrens[i].getAttribute('data-target'));   
   }
}});
