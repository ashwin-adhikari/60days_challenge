import PropTypes from 'prop-types'

function List() {
  const orders = [
    { id: 1, name: "Burger", calories: 200, category: "Snacks" },
    { id: 2, name: "Cocacola", calories: 150, category: "Drink" },
    { id: 3, name: "Fries", calories: 120, category: "Snacks" },
    { id: 4, name: "Cookies", calories: 100, category: "Snacks" },
  ];
  // orders.sort((a,b)=> a.name.localeCompare(b.name));//alphabetical order
  // orders.sort((a,b)=> b.name.localeCompare(a.name));//reverse alphabetical order
  // orders.sort((a,b)=>a.calories-b.calories);//numeric
  // orders.sort((a,b)=>b.calories-a.calories);//reverse numeric

  // const lowCalSnacks = orders.filter(order => order.calories<120);
  // const highCalSnacks = orders.filter(order => order.calories>120);

  const listitems = orders.map((order) => (
    <li key={order.id}>
      {order.name}: &nbsp;
      <b>{order.calories}</b> &nbsp;
      <i>{order.category}</i>
    </li>
  ));

  return (<>{orders.length > 0 && <ol>{listitems}</ol>}</>);
}
List.proptypes = {
    name: PropTypes.string,
    calories: PropTypes.number,
    category: PropTypes.string,
}

export default List;
