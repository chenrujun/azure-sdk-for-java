/**
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for
 * license information.
 *
 * Code generated by Microsoft (R) AutoRest Code Generator.
 */

package com.microsoft.azure.management.monitor.v2019_11_01.implementation;

import org.joda.time.DateTime;
import com.microsoft.azure.management.monitor.v2019_11_01.ErrorResponseCommon;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * The status of operation.
 */
public class OperationStatusInner {
    /**
     * The operation Id.
     */
    @JsonProperty(value = "id")
    private String id;

    /**
     * The operation name.
     */
    @JsonProperty(value = "name")
    private String name;

    /**
     * Start time of the job in standard ISO8601 format.
     */
    @JsonProperty(value = "startTime")
    private DateTime startTime;

    /**
     * End time of the job in standard ISO8601 format.
     */
    @JsonProperty(value = "endTime")
    private DateTime endTime;

    /**
     * The status of the operation.
     */
    @JsonProperty(value = "status")
    private String status;

    /**
     * The error detail of the operation if any.
     */
    @JsonProperty(value = "error")
    private ErrorResponseCommon error;

    /**
     * Get the operation Id.
     *
     * @return the id value
     */
    public String id() {
        return this.id;
    }

    /**
     * Set the operation Id.
     *
     * @param id the id value to set
     * @return the OperationStatusInner object itself.
     */
    public OperationStatusInner withId(String id) {
        this.id = id;
        return this;
    }

    /**
     * Get the operation name.
     *
     * @return the name value
     */
    public String name() {
        return this.name;
    }

    /**
     * Set the operation name.
     *
     * @param name the name value to set
     * @return the OperationStatusInner object itself.
     */
    public OperationStatusInner withName(String name) {
        this.name = name;
        return this;
    }

    /**
     * Get start time of the job in standard ISO8601 format.
     *
     * @return the startTime value
     */
    public DateTime startTime() {
        return this.startTime;
    }

    /**
     * Set start time of the job in standard ISO8601 format.
     *
     * @param startTime the startTime value to set
     * @return the OperationStatusInner object itself.
     */
    public OperationStatusInner withStartTime(DateTime startTime) {
        this.startTime = startTime;
        return this;
    }

    /**
     * Get end time of the job in standard ISO8601 format.
     *
     * @return the endTime value
     */
    public DateTime endTime() {
        return this.endTime;
    }

    /**
     * Set end time of the job in standard ISO8601 format.
     *
     * @param endTime the endTime value to set
     * @return the OperationStatusInner object itself.
     */
    public OperationStatusInner withEndTime(DateTime endTime) {
        this.endTime = endTime;
        return this;
    }

    /**
     * Get the status of the operation.
     *
     * @return the status value
     */
    public String status() {
        return this.status;
    }

    /**
     * Set the status of the operation.
     *
     * @param status the status value to set
     * @return the OperationStatusInner object itself.
     */
    public OperationStatusInner withStatus(String status) {
        this.status = status;
        return this;
    }

    /**
     * Get the error detail of the operation if any.
     *
     * @return the error value
     */
    public ErrorResponseCommon error() {
        return this.error;
    }

    /**
     * Set the error detail of the operation if any.
     *
     * @param error the error value to set
     * @return the OperationStatusInner object itself.
     */
    public OperationStatusInner withError(ErrorResponseCommon error) {
        this.error = error;
        return this;
    }

}
