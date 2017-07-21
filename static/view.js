  //create task
let create = false;
let present = true;

function createBucket(text,title){
  if (present){
    $.ajax({
      type:'POST',
      url:"http://localhost:5000/view",
      data:{
        method:"create",
        itemBody:text,
        title:title
      },
      success:function(response){
        console.log("data was sent and received",response);
        create = true
        response.forEach(function(itemObject){
          var markup = '<div class="list-item"><span>'+ itemObject.body +'</span><button class="close">x</button></div>';
          $('#items-list').append(markup);        
        })
      },
      error:function(err){
        console.log("error",err)
      }
    })
  $('#add-item-input').val('');
  }else{
    let markup = "<div id='bucket-list'><input type='text' id='title-input' name='title' placeholder='Name of the bucket' required><form id='add-item-form'><input id= 'add-item-input' type='text' name='add-item-input' required><button>Add an Item</button> </form><div id='items-list'></div><button id='delete-button'>DELETE</button></div>"
    $('bucket-lists').append(markup)
    present = true
  }
}


function createItem(text){
    let items = "";
    //ajax request to send data to server
    $.ajax({
      type:'POST',
      url:"http://localhost:5000/view",
      data:{
        method:"add",
        data:text
      },
      success:function(response){
        console.log("data was sent and received",response);
        $('#items-list').html("")
        response.forEach(function(itemObject){
          var markup = '<div class="list-item"><span>'+ itemObject.body +'</span><button class="close">x</button></div>';
          $('#items-list').append(markup);
        })
      },
      error:function(err){
        console.log("error",err)
      }
    })
    $('#add-item-input').val('');
}


$("#add-item-form").on('submit',function(e){
  e.preventDefault()
  var text = $('#add-item-input').val()
  var title = $('#title-input').val()
  console.log("these are text and title",text,title)
  if(text && title){
    if (create) {
      createItem(text)
    }else{
      createBucket(text,title)
    }
  }else{
    return
  }
})


$('#delete-button').on('click',function(e){
  e.preventDefault()
  if (create){
    alert("Are you sure you want to delete the bucket?")
      $.ajax({
        type:'POST',
        url:"http://localhost:5000/view",
        data:{
          method:"delete"
        },
        success:function(response){
          console.log("data was sent and received",response);
            $('.bucket-lists').html("")
        },
        error:function(err){
          console.log("error",err)
        }
      })
      present = false
      create = false
  }else{
    return
  }   
})

$('#items-list').on("click",".close",function(){
  let div = this.parentElement;
  let item = $(this).index()
  console.log("this is index",item)
  div.style.display = "none";
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
$(document).on('submit', '#title', function() {
    $(this).removeAttr('disabled');
});

$(document).on('click', '#title', function() {
    $(this).removeAttr('disabled');
});
*/