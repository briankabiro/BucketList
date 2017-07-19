//create task
function createItem(text){
    
    var items = "";
    $.ajax({
      type:'POST',
      url:"http://localhost:5000/view",
      data:{
        method:"add",
        data:text
      },
      success:function(response){
        console.log("data was sent and received",response);
        items = response;
        for (var key in response){
          console.log(response[key])
          var markup = '<li><div class="list-item"><span>'+ response[key] +'</span><div class="close">x</div></div></li>';
          $('#items-list').append(markup);
        }
      },
      error:function(err){
        console.log("error",err)
      }
    })
    
    $('#add-item-input').val('');
}

$(document).on('submit', '#title', function() {
    $(this).removeAttr('disabled');
});

$("#add-item-form").on('submit',function(e){
	e.preventDefault()
  var text = $('#add-item-input').val()
  if(text){
    createItem(text)
  }else{
    return
  }
})

/* 
  when add button pressed
  add input title and create button to DOM
  when create is pressed 
  send data to server and create bucket list
  return bucketlist with input and button for adding
  render bucketlist on frontend

  send add item request to server
  add item to bucket list
  return bucket list

  send delete item request to server
  find a way to get id of the item from the DOM
  delete item from bucketlist
  return bucketlist
*/