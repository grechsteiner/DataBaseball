import React from "react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

// Leaderboard page

function Leaderboard() {
  const [listOfPlayers, setListOfPlayers] = useState({
    battingLeaders: [],
    pitchingLeaders: [],
    fieldingLeaders: [],
  });
  const [battingStatistic, setBattingStatistic] = useState("G");
  const [pitchingStatistic, setPitchingStatistic] = useState("IP");
  const [fieldingStatistic, setFieldingStatistic] = useState("Inn");

  const [batYearID, setBatYearID] = useState(2023);
  const [pitchYearID, setPitchYearID] = useState(2023);
  const [fieldYearID, setFieldYearID] = useState(2023);

  const [batOrderDirection, setBatOrderDirection] = useState("desc");
  const [pitchOrderDirection, setPitchOrderDirection] = useState("desc");
  const [fieldingOrderDirection, setFieldingOrderDirection] = useState("desc");

  useEffect(() => {
    const url = `http://localhost:3001/leaderboard?battingStatistic=${encodeURIComponent(battingStatistic)}&pitchingStatistic=${encodeURIComponent(pitchingStatistic)}&fieldingStatistic=${encodeURIComponent(fieldingStatistic)}&battingYearID=${encodeURIComponent(batYearID)}&pitchingYearID=${encodeURIComponent(pitchYearID)}&fieldingYearID=${encodeURIComponent(fieldYearID)}&battingOrderDirection=${encodeURIComponent(batOrderDirection)}&pitchingOrderDirection=${encodeURIComponent(pitchOrderDirection)}&fieldingOrderDirection=${encodeURIComponent(fieldingOrderDirection)}`;

    try {
      fetch(url, {
        headers: {
          accessToken: sessionStorage.getItem("accessToken"),
        },
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else {
            console.log("FETCH failed", res.status);
          }
        })
        .then((data) => {
          if (data.error) {
            console.log(data.error);
          } else {
            console.log("FETCHED:", data)
            setListOfPlayers(data);
          }
        })
        .catch((error) => console.log("ERROR", error));
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }, [
    battingStatistic,
    pitchingStatistic,
    fieldingStatistic,
    batYearID,
    pitchYearID,
    fieldYearID,
    batOrderDirection,
    pitchOrderDirection,
    fieldingOrderDirection,
  ]);

  // Generate an array of years from 1871 to 2023
  const allYears = [];
  for (let y = 1871; y <= 2023; y++) {
    allYears.push(y);
  }

  return (
    <div>
      <div className="pageTitle">
        <h2>Leaderboard</h2>
      </div>

      <div className="subTitle">
        <h4>Batting</h4>
      </div>
      <div className="dropdown">
        <select
          value={battingStatistic}
          onChange={(e) => setBattingStatistic(e.target.value)}
        >
          <option value="G">G</option>
          <option value="PA">PA</option>
          <option value="AB">AB</option>
          <option value="R">R</option>
          <option value="H">H</option>
          <option value="2B">2B</option>
          <option value="3B">3B</option>
          <option value="HR">HR</option>
          <option value="RBI">RBI</option>
          <option value="SB">SB</option>
          <option value="CS">CS</option>
          <option value="BB">BB</option>
          <option value="SO">SO</option>
          <option value="IBB">IBB</option>
          <option value="HBP">HBP</option>
          <option value="SH">SH</option>
          <option value="SF">SF</option>
          <option value="GIDP">GIDP</option>
        </select>

        <select
          className="dropdown"
          value={batYearID}
          onChange={(e) => setBatYearID(parseInt(e.target.value, 10))}
        >
          {allYears.map((year) => (
            <option key={year} value={year}>
              {" "}
              {year}{" "}
            </option>
          ))}
        </select>

        <select
          className="dropdown"
          value={batOrderDirection}
          onChange={(e) => setBatOrderDirection(e.target.value)}
        >
          <option value="desc">Descending</option>
          <option value="asc">Ascending</option>
        </select>
      </div>

      <div className="Players">
        <div className="NameList">
          {listOfPlayers.battingLeaders.map((player, key) => (
            <div className="player" key={key}>
              <ul id="hittingList">
                <li>{player[battingStatistic]}</li>
                <li>
                  <Link to={`/players/${player.playerID}`}>
                    {player.nameFirst} {player.nameLast}
                  </Link>
                </li>
              </ul>
            </div>
          ))}
          <h3 className="ListWrap"> </h3>
        </div>
      </div>

      {/* ==================================================================================== */}

      <div className="subTitle">
        <h4>Pitching</h4>
      </div>

      <div className="dropdown">
        <select
          value={pitchingStatistic}
          onChange={(e) => setPitchingStatistic(e.target.value)}
        >
          <option value="IP">IP</option>
          <option value="G">G</option>
          <option value="W">W</option>
          <option value="L">L</option>
          <option value="GS">GS</option>
          <option value="CG">CG</option>
          <option value="SHO">SHO</option>
          <option value="SV">SV</option>
          <option value="H">H</option>
          <option value="R">R</option>
          <option value="ER">ER</option>
          <option value="HR">HR</option>
          <option value="BB">BB</option>
          <option value="IBB">IBB</option>
          <option value="SO">SO</option>
          <option value="HBP">HBP</option>
          <option value="BK">BK</option>
          <option value="WP">WP</option>
        </select>

        <select
          className="dropdown"
          value={pitchYearID}
          onChange={(e) => setPitchYearID(parseInt(e.target.value, 10))}
        >
          {allYears.map((year) => (
            <option key={year} value={year}>
              {" "}
              {year}{" "}
            </option>
          ))}
        </select>

        <select
          className="dropdown"
          value={pitchOrderDirection}
          onChange={(e) => setPitchOrderDirection(e.target.value)}
        >
          <option value="desc">Descending</option>
          <option value="asc">Ascending</option>
        </select>
      </div>

      <div className="Players">
        <div className="NameList">
          {listOfPlayers.pitchingLeaders.map((player) => (
            <div className="player" key={player.playerID}>
              <ul id="pitchingList">
                <li>{player[pitchingStatistic]}</li>
                <li>
                  <Link to={`/players/${player.playerID}`}>
                    {player.nameFirst} {player.nameLast}
                  </Link>
                </li>
              </ul>
            </div>
          ))}
          <h3 className="ListWrap"> </h3>
        </div>
      </div>

      <div className="subTitle">
        <h4>Fielding</h4>
      </div>

      <div className="dropdown">
        <select
          value={fieldingStatistic}
          onChange={(e) => setFieldingStatistic(e.target.value)}
        >
          <option value="Inn">Inn</option>
          <option value="GS">GS</option>
          <option value="PO">PO</option>
          <option value="A">A</option>
          <option value="E">E</option>
          <option value="DP">DP</option>        
        </select>

        <select
          className="dropdown"

          
          value={fieldYearID}
          onChange={(e) => setFieldYearID(parseInt(e.target.value, 10))}
        >
          {allYears.map((year) => (
            <option key={year} value={year}>
              {" "}
              {year}{" "}
            </option>
          ))}
        </select>

        <select
          className="dropdown"
          value={fieldingOrderDirection}
          onChange={(e) => setFieldingOrderDirection(e.target.value)}
        >
          <option value="desc">Descending</option>
          <option value="asc">Ascending</option>
        </select>
      </div>

      <div className="Players">
        <div className="NameList">
          {listOfPlayers.fieldingLeaders.map((player, key) => (
            <div className="player" key={key}>
              <ul>
                <li>{player[fieldingStatistic]}</li>
                <li>
                  <Link to={`/players/${player.playerID}`}>
                    {player.nameFirst} {player.nameLast}
                  </Link>
                </li>
              </ul>
            </div>
          ))}
          <h3 className="ListWrap"> </h3>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
