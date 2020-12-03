var MainTodoContainer = document.getElementById('todos');
var input = document.querySelector('.todo_input');
var addingButton = document.querySelector('.add-item');
var deleteAllBtn = document.querySelector('.deleteBtn');

addingButton.addEventListener('click',(e)=>{
    // console.log("hello word");
    // create element list
    if(input.value.trim()){
        // ul tag
        var ulTag = document.createElement('ul');
        ulTag.classList.add('todo-list-container');
        
        // todo list div
        var todoList = document.createElement('div');
        todoList.classList.add('todo-list');

        // li tag
        var liTag = document.createElement('li');
        liTag.innerHTML = input.value;
        liTag.classList.add('todo-item');

        // button div
        var buttonDiv = document.createElement('div');
        buttonDiv.classList.add('button');

        // completed button element
        var completeButton = document.createElement('button');
        completeButton.classList.add('completed');
        completeButton.innerHTML = '<i class="fa fa-check" ></i>';
        // edit button element
        var eidtButton = document.createElement('button');
        eidtButton.classList.add('editBtn');
        eidtButton.innerHTML = '<i class="fa fa-edit" ></i>';
        eidtButton.onclick = function(){
            editWorking(liTag);
        }
        // completed button element
        var traceButton = document.createElement('button');
        traceButton.classList.add('trashBtn');
        traceButton.innerHTML = '<i class="fa fa-trash" ></i>';
        
        // appending element into each other
        ulTag.appendChild(todoList);
        todoList.appendChild(liTag);
        todoList.appendChild(buttonDiv);
        buttonDiv.appendChild(completeButton);
        buttonDiv.appendChild(eidtButton);
        buttonDiv.appendChild(traceButton); 

        // add all element in main div
        MainTodoContainer.appendChild(ulTag);

        todoList.addEventListener('click',function(e){
            var items = e.target;
            if(items.classList[0] === 'completed'){
                var todo = items.parentElement;
                var todo2 = todo.parentElement;
                todo2.classList.add('line_through');
            }
            else if(items.classList[0] === 'trashBtn'){
                var todo = items.parentElement;
                var todo2 = todo.parentElement;
                var todo3 = todo2.parentElement
                todo3.classList.add('fall');
                todo3.addEventListener('transitionend',()=>{
                    todo3.remove();
                });
            }
        });

        input.value = "";
    }
    else if(input.value == ''){
        alert("Fill the input field..");
    }
});


function editWorking(e){
    var editValue = prompt('edit the selected item', e.firstChild.nodeValue);
    e.firstChild.nodeValue = editValue;
}


function deleteAllElements(){
    var gettingUlTag = document.querySelectorAll('.todo-list-container');
    for(var i = 0; i < gettingUlTag.length ; i++ ){
        gettingUlTag[i].remove();
    }
}