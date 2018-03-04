import React from 'react';
import { List } from 'material-ui/List';
import VideoListItem from './VideoListItem';

const VIDEOS = ['Видео 1', 'Видео 2', 'Видео 3'];

class VideoList extends React.Component {
    render() {
        const videoList = VIDEOS.map(item => <VideoListItem name={ item } />);

        return (
            <div className="video-list">
                <List>{ videoList }</List>
            </div>
        );
    }
}

export default VideoList;
