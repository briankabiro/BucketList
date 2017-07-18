//create task
function createItem(text){
    var markup = '<li><div class="checkbox"><label><input type="checkbox" value="" />'+ text +'</label></div></li>';
    $('#items-list').append(markup);
    $('#add-item-input').val('');
}

$("#add-item-form").on('submit',function(e){
	e.preventDefault()
  var text = $('#add-item-input').val()
  if(text){
    createItem(text)
  }else{
    return
  }
})
