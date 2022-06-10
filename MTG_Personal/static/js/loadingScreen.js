

const spinnerBox = document.getElementById('spinner-box')
const dataBox = document.getElementById('data-box')

$.ajax({
    type: 'GET',
    url: '/json_data/',
    success: function(response){
        setTimeout(()=>{
            dataBox.classList.remove('hidden')
            spinnerBox.classList.add('hidden')           
        },2000)
        
        
    },
    error: function(error){
        console.log(error)
    }
})