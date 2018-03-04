import React from 'react';
import PropTypes from 'prop-types';
import IconButton from 'material-ui/IconButton';
import ThumbUp from 'material-ui/svg-icons/action/thumb-up';
import ThumbDown from 'material-ui/svg-icons/action/thumb-down';


class VideoListItem extends React.Component {
    state = {
        likes: 0,
        dislikes: 0,
    };

    handleLike = () =>  {
        this.setState({ likes: this.state.likes + 1 });
    };

    handleDislike = () => {
        this.setState({ dislikes: this.state.dislikes + 1 });
    };

    styles = {
        largeIcon: {
            width: 48,
            height: 48,
        },
    };

    render() {
        const likePercentage = (this.state.likes / (this.state.likes + this.state.dislikes)) * 100;
        const dislikePercentage = (this.state.dislikes / (this.state.likes + this.state.dislikes)) * 100;

        return (
            [
                <video controls>
                    <source src="/static/_videos/tmp-video.mp4" />
                </video>,
                <div id="rate-panel">
                    <div id="rate-panel-left-side">
                        <IconButton className="rate-button" onClick={ this.handleLike } iconStyle={ this.styles.largeIcon }>
                            <ThumbUp color='#5CB85C' />
                        </IconButton>
                        <h2 className="rate-click-number">{ this.state.likes }</h2>
                        <IconButton className="rate-button" onClick={ this.handleDislike } iconStyle={ this.styles.largeIcon }>
                            <ThumbDown color='#D7524E' />
                        </IconButton>
                        <h2 className="rate-click-number">{ this.state.dislikes }</h2>
                    </div>
                    <div id="rate-panel-left-side">
                        <div id="like-percentage-line" style={ { 'width': `${ likePercentage }%` } } />
                        <div id="dislike-percentage-line" style={ { 'width': `${ dislikePercentage }%` } } />
                    </div>
                </div>,
            ]
        );
    }
}

export default VideoListItem;
