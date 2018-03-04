import React from 'react';
import { ListItem } from 'material-ui/List';
import PropTypes from 'prop-types';


class VideoListItem extends React.Component {
    static propTypes = {
        name: PropTypes.string.isRequired,
    };

    render() {
        return (
            <ListItem className="video-list-item" primaryText={ this.props.name } />
        );
    }
}

export default VideoListItem;
