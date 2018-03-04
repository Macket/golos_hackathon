import React from 'react';
import { List } from 'material-ui/List';
import PropTypes from 'prop-types';
import VideoListItem from './VideoListItem';
import CircularProgress from 'material-ui/CircularProgress';

class VideoList extends React.Component {
    static propTypes = {
        videoList: PropTypes.arrayOf(PropTypes.shape(VideoListItem.propTypes)),
        isLoading: PropTypes.bool,
        fetchVideo: PropTypes.func.isRequired,
    };

    static defaultProps = {
        videoList: [],
        isLoading: false,
    };

    render() {
        const videoList = this.props.videoList.map(item =>
            <VideoListItem name={ item.name } fetchVideo={ this.props.fetchVideo } />);
        if (this.props.isLoading) {
            return (
                <CircularProgress />
            );
        }
        return (
            <div className="video-list">
                <List>{ videoList }</List>
            </div>
        );
    }
}

export default VideoList;
