let nav = 0;
let clicked = null;
let events = localStorage.getItem('events') ? JSON.parse(localStorage.getItem('events')) : [];

const calendar = document.getElementById('calendar');
const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
const newEventModal = document.getElementById('newEventModal');
const backDrop = document.getElementById('modalBackDrop');
const nameInput = document.getElementById('nameInput');

function load() {

    const dt = new Date();

    if (nav !== 0){
        dt.setMonth(new Date().getMonth() + nav);
    }

    const day = dt.getDate();
    const month = dt.getMonth(); //array index for months
    const year = dt.getFullYear();
    const firstDayOfMonth = new Date(year, month, 1);
    const daysInMonth = new Date(year, month+1, 0).getDate();
    
    //get the day of the week that the first day of the month lands on
    const dateString = firstDayOfMonth.toLocaleDateString('en-us', {
        weekday: 'long',
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',
    });
    
    //account for the "padding days" of the month 
    const paddingDays = weekdays.indexOf(dateString.split(', ')[0]);
    
    //print the month and date on the dashboard
    document.getElementById('monthDisplay').innerText = 
        `${dt.toLocaleDateString('en-us', {month: 'long'})} ${year}`;

    calendar.innerHTML = ''; //wipes day and padding squares before loading next month
    //render the 'padding days' for all months
    //render empty squares for the # of 'padding days' in the month
    for(let i = 1; i <= paddingDays + daysInMonth; i++){
        const daySquare = document.createElement('div');
        daySquare.classList.add('day');
        //iterated past the # of padding days, then print days of week 
        if(i > paddingDays){
            daySquare.innerText = i - paddingDays;
            daySquare.addEventListener('click', () => openModal(`${month + 1}/${i-paddingDays}/${year}`));
        }
        // i is less than # of padding days, print padding day
        else{
            daySquare.classList.add('padding');
        }
        calendar.appendChild(daySquare);
    }
    //console.log(dateString);
}

function backButton(){
    nav--;
    console.log(nav);
    load();
}

function nextButton(){
    nav++;
    console.log(nav);
    load();
}

function openModal(date) {
    clicked = date;

    const eventForDay = events.find(e => e.date === clicked);

    if (eventForDay){
        console.log('Word Order already created for this day');
    }
    else {
        newEventModal.style.display = 'block';
    }
    backDrop.style.display = 'block';
}

function saveWorkOrder(){

    if(nameInput.value){
        nameInput.classList.remove('error');

        events.push({
            date: clicked,
            name: nameInput.value,
        });

        localStorage.setItem('events',JSON.stringify(events));
        closeModal();
    }
    else{
        nameInput.classList.add('error');
    }
 
}

//function edit WorkOrder(){}


function closeModal(){
    nameInput.classList.remove('error');
    newEventModal.style.display = 'none';
    backDrop.style.display = 'none';
    nameInput.value = '';
    clicked = null;
    load();
}

load();

