import React from 'react';
import AppBar from 'material-ui/AppBar';
import TextField from 'material-ui/TextField';
import PropTypes from "prop-types";
import apiUrls from "../constants/apiUrls";

const styles = {
    appBar: {
        backgroundColor: 'white',
    },
    title: {
        cursor: 'pointer',
        color: 'black',
    },
    icon: {
        cursor: 'pointer',
        color: 'black',
    },
};

class VideoList extends React.Component {
    static propTypes = {
        searchVideos: PropTypes.func.isRequired,
    };

    state = {
        query: '',
    };

    componentDidMount() {
        document.getElementById('search').addEventListener('keydown', this.handleKeyDown);
    }

    handleKeyDown = (e) => {
        if (e.keyCode === 13) { // Enter
            this.props.searchVideos(this.state.query);
        }
    };

    handleChange = (e) => {
        this.setState({ query: e.target.value });
    };

    render() {
        return (
            <AppBar
                style={ styles.appBar }
                title={ <span style={ styles.title }>Зрение</span> }
                iconElementLeft={ <img src="/static/logo.jpg" width="40" height="40" /> }
                iconElementRight={ <TextField
                    id="search"
                    value={ this.state.query }
                    style={ { 'margin-right': '150px' } }
                    onChange={ this.handleChange }
                    hintText="Поиск"
                /> }
            />
        );
    }
}

export default VideoList;

