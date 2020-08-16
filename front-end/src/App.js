import React ,{ useState , useEffect} from 'react';
import './App.css';
import { Redirect, Link, Route,Switch } from 'react-router-dom'
import {  MenuItem,  FormControl,  Select} from "@material-ui/core";
import InfoBox from "./InfoBox";
import StockInfo from "./StockInfo";
import Graph from "./Graph";

function App() {

  const [ticker, setTicker] = useState("NSE");
  const [stock, setStock] = useState({});
  const [Stockdata, setData] = useState({});
  
  

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/get-data/NSE/")
      .then((response) => response.json())
      .then((data) => {
        setStock(data.data[0]);
        setData(data.data[1]);

      });
  }, []);

  const onStockChange = async   (e) => {
  const tickerSymbol = e.target.value;
    const url =
      tickerSymbol === "NSE"
        ? "http://127.0.0.1:8000/api/get-data/NSE/"
        : "http://127.0.0.1:8000/api/get-data/BSE/";
    // const url = "http://127.0.0.1:8000/api/get-data/NSE/"
    await fetch(url)
      .then((response) => response.json())
      .then((data) => {
        setTicker(tickerSymbol);
        setStock(data.data[0]);
        setData(data.data[1]);

      });
  };

  const [closePrice, setClosePrice] =useState();
  const [companyName, setCompanyName] =useState("Reliance");

  const onCompanyChange = (e) => {
    const companyname = e.target.value;
      setCompanyName(companyname);
    };


  return (
    <div className="app">
        <div className="app__header">
          
          <FormControl className="app__dropdown">
            <Select
              variant="outlined"
              onChange={onStockChange}
              value = {ticker}
            >
              <MenuItem value="NSE">NSE</MenuItem>
              <MenuItem value="BSE">BSE</MenuItem>
             
            </Select>
          </FormControl>
          <h1>Flipr Hackathon 5</h1>
        </div>
        <div className="app__stats">
          
          <InfoBox
            market= {ticker}
            date = {parseFloat(Stockdata[0]).toFixed(2)  }
            todayStock={parseFloat(Stockdata[4]).toFixed(2)}
            prevStock={parseFloat(stock[4]).toFixed(2)}
            
          />
        </div>
        <StockInfo
          date = {Stockdata[0]}
          type= {ticker} 
          open={parseFloat(Stockdata[1]).toFixed(2)} 
          todayStock={parseFloat(Stockdata[4]).toFixed(2)} 
          prevStock = {parseFloat(stock[4]).toFixed(2)}
          low = {parseFloat(Stockdata[2]).toFixed(2)}
          high = {parseFloat(Stockdata[3]).toFixed(2)}
        />
        <div className="app__graph">
        <FormControl className="appgraph__dropdown">
            <Select
              variant="outlined"
              onChange={onCompanyChange}
              value = {companyName}
            >
              <MenuItem value="Reliance">Reliance</MenuItem>
              <MenuItem value="AshokLeyland">Ashok Leyland</MenuItem>
              <MenuItem value="Cipla">Cipla</MenuItem>
              <MenuItem value="TataSteel">Tata Steel</MenuItem>
              <MenuItem value="EicherMotors">Eicher Motors</MenuItem>
             
            </Select>
          </FormControl>

          <Graph casesType={companyName} />
          
        </div>
    </div>
  );
};

export default App;
