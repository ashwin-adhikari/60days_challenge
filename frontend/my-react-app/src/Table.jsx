import PropTypes from 'prop-types'


function Table(props){
    return(
        <div className="table">
            <p>Table Capacity:{props.capacity}</p>
            <p>Occupancy:{props.isOccupied ? "Occupied" : "Empty"}</p>
            <p>Location:{props.location}</p>
        </div>
    );


}
Table.proptypes= {
    capacity: PropTypes.number,
    isOccupied: PropTypes.bool,
    location: PropTypes.string,
}
Table.defaultProps = {
    capacity: 0,
    location: "NaN",
    isOccupied: true,
}
export default Table