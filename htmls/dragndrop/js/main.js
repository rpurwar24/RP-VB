$("tbody").sortable({
    items: "> tr",
    appendTo: "parent",
    helper: "clone",
    placeholder: "sortable-placeholder",
    deactivate: function(event,ui){
    	var prevId,nextId;
    	console.log('item which is moved has id - ',ui.item.context.id);
    	if(ui.item.context.nextElementSibling)
    		nextId = ui.item.context.nextElementSibling.id;
    	else
    		nextId = -1;
    	console.log('item below the moved item has id - ',nextId);
    	if(ui.item.context.previousElementSibling)
    		prevId = ui.item.context.previousElementSibling.id;
    	else
    		prevId = -1;
    	console.log('item above the moved item has id - ',prevId);
    }
}).disableSelection();