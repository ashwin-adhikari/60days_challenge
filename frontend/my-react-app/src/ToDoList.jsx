import { useState } from "react";

export default function ToDoList(){
    const [tasks, setTasks] = useState(["eat","sleep","repeat"])
    const [newTask, setNewTask] = useState("")

    function handleInputChange(e){
        setNewTask(e.target.value)
    }
    function addTask(e){
        if(newTask.trim()!==""){
            //this prevents adding of empty string
            setTasks(t=> [...t,newTask])
            setNewTask("")
        }
    }
    function deleteTask(index){
        const updatedTasks = tasks.filter((element, i)=> i !== index )
        setTasks(updatedTasks)
    }
    function moveTaskUp(index){

        if(index > 0){
            const updatedTasks = [...tasks];
            [updatedTasks[index],updatedTasks[index-1]] = [updatedTasks[index-1],updatedTasks[index]];
            //array destructuring
            setTasks(updatedTasks);
        }
    }
    function moveTaskDown(index){
        if(index > tasks.length-1){
            const updatedTasks = [...tasks];
            [updatedTasks[index],updatedTasks[index+1]] = [updatedTasks[index+1],updatedTasks[index]];
            //array destructuring
            setTasks(updatedTasks);
    }
    }
    return(
        <div className="to-do-list">
            <h1>To-Do-List</h1>
            <div>
                <input type="text" placeholder="Enter a text" value={newTask} onChange={handleInputChange}/>
                <button className="add-button" onClick={addTask}>Add</button>
            </div>

            <ol>
                {tasks.map((task,index) => 
                <li key={index}>
                    <span className="text">{task}</span>
                    <button className="delete-button" onClick={()=> deleteTask(index)}>Delete</button>
                    <button className="move-button" onClick={()=> moveTaskUp(index)}>Up</button>
                    <button className="move-button" onClick={()=> moveTaskDown(index)}>Down</button>
                    </li>
                )}
            </ol>
        </div>
    );
    }