import { isLocalFileSystem, warnOnDev } from 'utils/pdf/utils';
import Document from './Document';
import Outline from './Outline';
import Page from './Page';
import makeSetOptions from './setOptions';


if (isLocalFileSystem) {
  // eslint-disable-next-line no-console
  warnOnDev('You are running React-PDF from your local file system. PDF.js Worker may fail to load due to browser\'s security policies. If you\'re on Google Chrome, you can use --allow-file-access-from-files flag for debugging purposes.');
}

const pdfjs = require('pdfjs-dist/webpack');

const setOptions = makeSetOptions(pdfjs);

export {
  Document,
  Outline,
  Page,
  setOptions,
};
