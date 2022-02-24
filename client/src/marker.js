import "./App.css";
function Marker(props) {
  return (
    <div className="marker" style={{ backgroundColor: props.color }}></div>
  );
}

export default Marker;
