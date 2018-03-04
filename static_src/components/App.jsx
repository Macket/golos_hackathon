import React from 'react';
// import { Switch, Route } from 'react-router-dom';
import VideoList from './VideoList';
import VideoPlayer from './VideoPlayer';
import Header from './Header';
import '../styles/base.scss';


class App extends React.Component {
    render() {
        return (
            [<Header id="header" />,
                <div id="layout">
                    <div id="layout-left-side">
                        <VideoPlayer />
                    </div>
                    <div id="layout-right-side">
                        <VideoList />
                    </div>
                </div>]
        );
    }
}

export default App;
