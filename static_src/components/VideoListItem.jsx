import React from 'react';
import { ListItem } from 'material-ui/List';
import PropTypes from 'prop-types';
import apiUrls from '../constants/apiUrls';


class VideoListItem extends React.Component {
    static propTypes = {
        name: PropTypes.string,
        author: PropTypes.string,
        description: PropTypes.string,
        fetchVideo: PropTypes.func.isRequired,
    };

    static defaultProps = {
        name: '',
        author: '',
        description: '',
    };

    handleClick = (e) => {
        const url = `${apiUrls.video}?name=${e.target.innerHTML}`;
        this.props.fetchVideo(url);
    };

    render() {
        return (
            <ListItem className="video-list-item" primaryText={ this.props.name } onClick={ this.handleClick } />
        );
    }
}

export default VideoListItem;
