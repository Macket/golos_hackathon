import React from 'react';
// import { Switch, Route } from 'react-router-dom';
import VideoList from './VideoList';
import VideoPlayer from './VideoPlayer';
import Header from './Header';
import apiUrls from './../constants/apiUrls';
import '../styles/base.scss';


class App extends React.Component {
    state = {
        videoList: [],
        isLoadingList: false,
        isLoadingVideo: false,
    };

    componentWillMount() {
        this.setState({ isLoadingList: true });
        fetch(apiUrls.videos, {
            credentials: 'include',
        }).then(body => body.json(),
        ).then(json => this.setState({ videoList: json, isLoadingList: false }),
        );
    };

    fetchVideo = (url) => {
        this.setState({ isLoadingVideo: true });
        fetch(url, {
            credentials: 'include',
        }).then(body => body.json(),
        ).then(() => this.setState({ isLoadingVideo: false }),
        );
    };

    handleSearchVideo = (query) => {
        const url = `${apiUrls.videos}?query=${query}`;
        this.setState({ isLoadingList: true });
        fetch(url, {
            credentials: 'include',
        }).then(body => body.json(),
        ).then(json => this.setState({ videoList: json, isLoadingList: false }),
        );
    };

    render() {
        return (
            [<Header id="header" searchVideos={ this.handleSearchVideo }/>,
                <div id="layout">
                    <div id="layout-left-side">
                        <VideoPlayer isLoading={ this.state.isLoadingVideo } />
                    </div>
                    <div id="layout-right-side">
                        <VideoList
                            videoList={ this.state.videoList }
                            isLoading={ this.state.isLoadingList }
                            fetchVideo={ this.fetchVideo }
                        />
                    </div>
                </div>]
        );
    }
}

export default App;
